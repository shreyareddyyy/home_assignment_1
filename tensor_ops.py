import tensorflow as tf

# 1. Create a random tensor of shape (4, 6)
tensor = tf.random.uniform((4, 6))
print("Original Tensor:\n", tensor)

# 2. Rank and shape
rank = tf.rank(tensor)
shape = tf.shape(tensor)
print("Rank:", rank.numpy())
print("Shape:", shape.numpy())

# 3. Reshape to (2, 3, 4) and Transpose to (3, 2, 4)
reshaped = tf.reshape(tensor, (2, 3, 4))
transposed = tf.transpose(reshaped, perm=[1, 0, 2])
print("Reshaped Shape:", reshaped.shape)
print("Transposed Shape:", transposed.shape)

# 4. Broadcasting
small_tensor = tf.constant([[1, 2, 3, 4]], dtype=tf.float32)
broadcasted_sum = transposed + small_tensor  # Broadcasts to (3, 2, 4)
print("Broadcasted Tensor Addition Result:\n", broadcasted_sum)