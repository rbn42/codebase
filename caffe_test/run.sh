cd ~/caffe/examples
mkdir mnist

../scripts/download_model_binary.py ../models/bvlc_reference_caffenet

./data/mnist/get_mnist.sh
./examples/mnist/create_mnist.sh
