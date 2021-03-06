from __future__ import division
from __future__ import print_function

import argparse
import sys

import ambodiReadData as dataset


import tensorflow as tf

FLAGS = None


def main(_):
    """Run the NN."""
    mnist = dataset.read_data_sets(FLAGS.data_dir, one_hot=True)

    x = tf.placeholder(tf.float32, [None, 10000])
    w = tf.Variable(tf.zeros([10000, 5000]))
    b = tf.Variable(tf.zeros([5000]))
    y = tf.matmul(x, w) + b

    # Define loss and optimizer
    y_ = tf.placeholder(tf.float32, [None, 5000])

    # The raw formulation of cross-entropy,
    #
    #   tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(tf.nn.softmax(y)),
    #                                 reduction_indices=[1]))
    #
    # can be numerically unstable.
    #
    # So here we use tf.nn.softmax_cross_entropy_with_logits on the raw
    # outputs of 'y', and then average across the batch.
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y, labels=y_))
    # cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y,y_)) #original
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

    sess = tf.InteractiveSession()
    tf.global_variables_initializer().run()
    # Train
    for _ in range(10):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        print(batch_xs.shape)
        print(batch_ys.shape)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

    # Test trained model
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print(sess.run(accuracy, feed_dict={x: mnist.test.images,
                                        y_: mnist.test.labels}))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default='/tmp/tensorflow/mnist/ \
        input_data', help='Directory for storing input data')
    FLAGS, unparsed = parser.parse_known_args()
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)