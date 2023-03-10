# MCL
Multiple-head Convolutional LSTM （MCL） 模型是具有multiple_heads的ConvLSTM(Convolutional LSTM)模型，
模型的每个One_head ConvLSTM都可以使用不同大小的卷积核读取输入时间步骤。
例如：在实验一中，我们使用了Three_head 的MCL模型，其中每一个One_head ConvLSTM我们分别使用了三种不同的卷积核 ((1,3)、(1,5)、(1,11))。
这样允许模型以三种不同的过滤器大小来读取和解释输入数据[8]。然后，三个One_head ConvLSTM的运行结果在合并层（merge）连接。并由全连接层(FC)进行预测运算。
