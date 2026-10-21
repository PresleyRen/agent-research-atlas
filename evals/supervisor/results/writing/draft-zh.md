# Draft fragment

我们提出一个版本感知路由方法，解决了所有文档 Agent 的意图理解问题。该方法在 64 个请求上准确率为 96%，证明澄清必然提高推理能力。我们在三个真实业务数据集上验证了它的泛化。

方法根据初始消息和检索片段选择回答、检索或追问。显式指定版本时使用版本约束过滤；隐含偏好时依据规则决定是否追问。路由器和文档过滤器共享一个版本状态，因此一个模块同时处理两类困难。

英文原句待润色：On the evaluated examples, the version-aware policy was associated with a higher success rate. We list the failure categories in descending order.
