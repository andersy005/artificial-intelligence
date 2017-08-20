import tensorflow as tf
import keras

a = tf.constant(5)
b = tf.constant(6)
c = tf.add(a, b)

with tf.Session() as sess:
  print(sess.run(c))
  
print("Test succeeded....")
