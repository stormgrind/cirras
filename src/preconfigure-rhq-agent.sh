#!/bin/sh

[ -f /etc/sysconfig/rhq ] && . /etc/sysconfig/rhq

RHQ_AGENT_NAME=rhq-enterprise-agent
RHQ_AGENT_VERSION=1.4.0.B01
RHQ_CONFIG=/usr/share/rhq/agent-configuration.xml
RHQ_TMP_DIR=/tmp/rhq-$RHQ_VERSION

IP_ADDRESS=`ip addr list eth0 | grep "inet " | cut -d' ' -f6 | cut -d/ -f1`

rm -rf $RHQ_TMP_DIR
mkdir -p $RHQ_TMP_DIR

cd $RHQ_TMP_DIR
jar xvf $RHQ_HOME/jbossas/server/default/deploy/rhq.ear.rej/rhq-downloads/rhq-agent/$RHQ_AGENT_NAME-$RHQ_AGENT_VERSION.jar $RHQ_AGENT_NAME-$RHQ_AGENT_VERSION.zip
unzip -q $RHQ_AGENT_NAME-$RHQ_AGENT_VERSION.zip -d $RHQ_TMP_DIR

## ADD HERE CHANGES TO agent-configuration.xml
sed s/#BIND_ADDRESS#/$IP_ADDRESS/g $RHQ_CONFIG > rhq-agent/conf/agent-configuration.xml

jar uvf $RHQ_AGENT_NAME-$RHQ_AGENT_VERSION.zip rhq-agent/conf/agent-configuration.xml
jar uvf $RHQ_HOME/jbossas/server/default/deploy/rhq.ear.rej/rhq-downloads/rhq-agent/$RHQ_AGENT_NAME-$RHQ_AGENT_VERSION.jar $RHQ_AGENT_NAME-$RHQ_AGENT_VERSION.zip

chown rhq:rhq /opt/rhq/ -R
