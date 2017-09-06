import tensorflow as tf

a = tf.constant(5)
b = tf.constant(6)
c = tf.add(a, b)

with tf.Session() as sess:
    assert sess.run(c) == 11
