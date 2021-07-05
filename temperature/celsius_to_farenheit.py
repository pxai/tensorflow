import tensorflow
import numpy

celsius = numpy.array([-40, -10, 0, 8, 15, 22, 38], dtype: float)
farenheit = numpy.array([-40, 14, 32, 46, 59, 72, 100], dtype: float)

layer = tensorflow.keras.layers.Dense(units=1, input_shape=[1])
model = tensorflow.keras.Sequential([layer])

model.compile(optimizer.keras.optimizers.Adam())
