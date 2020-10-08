import numpy
import scipy.special
def init_net():
    input_nodes=784
    print('Введите число скрытых нейронов: ')
    hidden_nodes=int(input())
    out_nodes=10
    print('Введите скорость обучения(0.5): ')
    lern_node=float(input())
    return input_nodes, hidden_nodes, out_nodes, lern_node
def creat_net(input_nodes,hidden_nodes,out_nodes):
    input_hidden_w=(numpy.random.rand(hidden_nodes,input_nodes)-0.5)
    hidden_out_w=(numpy.random.rand(out_nodes,hidden_nodes)-0.5)
    return input_hidden_w, hidden_out_w
def fun_active(x):
    return scipy.special.expit(x)
def query(input_hidden_w,hidden_out_w,inputs_list):
    inputs_sig=numpy.array(inputs_list,ndmin=2).T
    hidden_inputs=numpy.dot(input_hidden_w,inputs_sig)
    hidden_out=fun_active(hidden_inputs)
    final_inputs=numpy.dot(hidden_out_w,hidden_out)
    final_out=fun_active(final_inputs)
    return final_out
def treyn(targget_list,input_list,input_hidden_w,hidden_out_w,lern_node):
    targgets=numpy.array(targget_list,ndmin=2).T
    inputs_sig=numpy.array(input_list,ndmin=2).T
    hidden_inputs=numpy.dot(input_hidden_w,inputs_sig)
    hidden_out=fun_active(hidden_inputs)
    final_inputs=numpy.dot(hidden_out_w,hidden_out)
    final_out=fun_active(final_inputs)
    out_errors=targgets-final_out
    hidden_errors=numpy.dot(hidden_out_w.T, out_errors)
    hidden_out_w+=lern_node*numpy.dot((out_errors*final_out*(1-final_out)), numpy.transpose(hidden_out))
    input_hidden_w+=lern_node*numpy.dot((hidden_errors*hidden_out*(1-hidden_out)),numpy.transpose(inputs_sig))
    return hidden_out_w, input_hidden_w
def test_set(hidden_out_w,input_hidden_w):
    data_file=open('mnist_train.csv','r')
    trening_list=data_file.readlines()
    data_file.close()
    for record in trening_list:
        all_values=record.split(',')
        inputs=(numpy.asfarray(all_values[1:])/255.0*0.99)+0.01
        targets=numpy.zeros(10)+0.01
        targets[int(all_values[0])]=0.99
        hidden_out_w,input_hidden_w=treyn(targets,inputs,input_hidden_w,hidden_out_w,lern_node)
    data_file = open('mnist_test.csv', 'r')
    test_list = data_file.readlines()
    data_file.close()
    test = []
    for record in test_list:
        all_values=record.split(',')
        inputs=(numpy.asfarray(all_values[1:])/255.0*0.99)+0.01
        out_session=query(input_hidden_w,hidden_out_w,inputs)
        if int(all_values[0])==numpy.argmax(out_session):
            test.append(1)
        else:
            test.append(0)
    print(len(test))
    test=numpy.asarray(test)
    print('Эффективность сети % =',(test.sum()/test.size)*100)
    return hidden_out_w,input_hidden_w
input_nodes,hidden_nodes,out_nodes,lern_node=init_net()
input_hidden_w,hidden_out_w=creat_net(input_nodes,hidden_nodes,out_nodes)
for i in range(5):
    print('Test #',i+1)
    hidden_out_w, input_hidden_w=test_set(hidden_out_w,input_hidden_w)
