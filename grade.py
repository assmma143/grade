import tensorflow as tf


print('Enter the grade of student: ')
a1 = float(input('enter student 1 grade '))
a2 = float(input('enter student 2 grade '))
a3 = float(input('enter student 3 grade '))
a4 = float(input('enter student 4 grade '))


x1 = tf.constant([a1,a2,a3,a4])
x2 = tf.constant([0.25,0.25,0.25,0.25])


# Multiply
result = tf.multiply(x1, x2)


sess = tf.Session()


# Print the result
print(sess.run(result))

sess.close()
