import tensorflow
import numpy
import matplotlib.pyplot as plot

celsius = numpy.array([-40, -10, 0, 8, 15, 22, 38], dtype = float)
farenheit = numpy.array([-40, 14, 32, 46, 59, 72, 100], dtype = float)

hiddenLayer1 = tensorflow.keras.layers.Dense(units = 3, input_shape = [1])
hiddenLayer2 = tensorflow.keras.layers.Dense(units = 3, input_shape = [1])
output = tensorflow.keras.layers.Dense(units = 1)
model = tensorflow.keras.Sequential([hiddenLayer1, hiddenLayer2, output])

LEARNING_RATE = 0.1
model.compile(
    optimizer = tensorflow.keras.optimizers.Adam(LEARNING_RATE),
    loss = 'mean_squared_error'
)

print("Start learning...")
history = model.fit(celsius, farenheit, epochs = 1000, verbose = False)
print("Learning completed!!")

result = model.predict([100.0])
print("Prediction for 100.0 is %s" % result)

plot.xlabel("#Iteration")
plot.ylabel("#Loss")
plot.plot(history.history["loss"])
plot.show()
