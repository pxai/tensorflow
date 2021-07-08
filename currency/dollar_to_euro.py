import tensorflow
import numpy
import matplotlib.pyplot as plot

dollar = numpy.array([0, 2, 10, 15, 500], dtype = float)
euro = numpy.array([0, 1.68, 8.42, 12.64, 421.17], dtype = float)

layer = tensorflow.keras.layers.Dense(units = 1, input_shape = [1])
model = tensorflow.keras.Sequential([layer])
LEARNING_RATE = 0.1
model.compile(
    optimizer = tensorflow.keras.optimizers.Adam(LEARNING_RATE),
    loss = 'mean_squared_error'
)

print("Start learning...")
history = model.fit(dollar, euro, epochs = 1000, verbose = False)
print("Learning completed!!")

result = model.predict([100.0])
print("Prediction for 100.0 is %s" % result)

plot.xlabel("#Iteration")
plot.ylabel("#Loss")
plot.plot(history.history["loss"])
plot.show()
