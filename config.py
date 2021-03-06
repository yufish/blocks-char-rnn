config = {}
config['batch_size'] = 50  # number of samples taken per each update
config['hidden_size'] = 128  # number of hidden units per layer
config['num_layers'] = 2
config['learning_rate'] = 0.002
config['learning_rate_decay'] = 0.97 # set to 0 to not decay learning rate
config['decay_rate'] = 0.95  # decay rate for rmsprop
config['step_clipping'] = 1.0  # clip norm of gradients at this value
config['dropout'] = 0

config['model'] = 'gru'  # 'rnn', 'gru' or 'lstm'
config['nepochs'] = 30  # number of full passes through the training data
config['seq_length'] = 50  # number of chars in the sequence
config['hdf5_file'] = 'input.hdf5'  # hdf5 file with Fuel format
config['text_file'] = 'input.txt'  # raw input file
config['train_size'] = 0.95  # fraction of data that goes into train set
config['save_path'] = '{0}_best.tar'.format(config['model'])  # path to best model file
config['load_path'] = '{0}_saved.tar'.format(config['model'])  # start from a saved model file
config['last_path'] = '{0}_last.tar'.format(config['model'])  # path to save the model of the last iteration
