# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateFlowJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'CreateFlowJob')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_RunConf(self):
		return self.get_query_params().get('RunConf')

	def set_RunConf(self,RunConf):
		self.add_query_param('RunConf',RunConf)

	def get_EnvConf(self):
		return self.get_query_params().get('EnvConf')

	def set_EnvConf(self,EnvConf):
		self.add_query_param('EnvConf',EnvConf)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_Params(self):
		return self.get_query_params().get('Params')

	def set_Params(self,Params):
		self.add_query_param('Params',Params)

	def get_ParamConf(self):
		return self.get_query_params().get('ParamConf')

	def set_ParamConf(self,ParamConf):
		self.add_query_param('ParamConf',ParamConf)

	def get_FailAct(self):
		return self.get_query_params().get('FailAct')

	def set_FailAct(self,FailAct):
		self.add_query_param('FailAct',FailAct)

	def get_Mode(self):
		return self.get_query_params().get('Mode')

	def set_Mode(self,Mode):
		self.add_query_param('Mode',Mode)

	def get_RetryInterval(self):
		return self.get_query_params().get('RetryInterval')

	def set_RetryInterval(self,RetryInterval):
		self.add_query_param('RetryInterval',RetryInterval)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_MaxRetry(self):
		return self.get_query_params().get('MaxRetry')

	def set_MaxRetry(self,MaxRetry):
		self.add_query_param('MaxRetry',MaxRetry)

	def get_ProjectId(self):
		return self.get_query_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_query_param('ProjectId',ProjectId)

	def get_ParentCategory(self):
		return self.get_query_params().get('ParentCategory')

	def set_ParentCategory(self,ParentCategory):
		self.add_query_param('ParentCategory',ParentCategory)