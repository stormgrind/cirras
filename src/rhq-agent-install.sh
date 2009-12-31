#!/bin/sh

[ -f /etc/sysconfig/boxgrinder ] && . /etc/sysconfig/boxgrinder

RHQ_AGENT_HOME=/opt/rhq-agent

[ -f /etc/sysconfig/rhq-agent ] && . /etc/sysconfig/rhq-agent

[ "x$RHQ_SERVER_IP" = "x" ] && exit 0

RHQ_AGENT_JAR_LOCATION=http://$RHQ_SERVER_IP:7080/agentupdate/download

rm -rf $RHQ_AGENT_HOME
mkdir -p $RHQ_AGENT_HOME

sleep=0
downloaded=0
while [ "$downloaded" = "0" ]; do
    sleep 5
    sleep=`expr $sleep + 5`

    http_code=`curl -o /dev/null -s -m 5 -w '%{http_code}' $RHQ_AGENT_JAR_LOCATION`

    if [ $http_code -eq "200" ]
    then
        wget $RHQ_AGENT_JAR_LOCATION -O $RHQ_AGENT_HOME/rhq-agent.jar
        downloaded=1        
    fi
done

cd $RHQ_AGENT_HOME

java -jar rhq-agent.jar --install

sed -i s/#AGENT_NAME#/$APPLIANCE_NAME-$HOSTNAME/g $RHQ_AGENT_HOME/rhq-agent/conf/agent-configuration.xml
