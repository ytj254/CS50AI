# "CS50AI Project 5 Traffic" Experimentation Process Record 

## Operating environment: Windows 10 Home, AMD Ryzen 7 5800H, Nvidia GeForce RTX 3070 laptop GPU

This is the test process document for implementing CS50AI project 5 Traffic.

### Test 1. Just use the structure in the course  
    
Convolutional layer: Conv2D(32, (3, 3), activation='relu', input_shape=(30, 30, 3))  
Max-pooling layer: MaxPooling2D(pool_size=(2, 2))  
Hidden layer: Dense(128, activation='relu'), with dropout (tf.keras.layers.Dropout(0.5)  
Output layer: Dense(NUM_CATEGORIES, activation='softmax') 

#### Result: 
    Epoch 10/10
    500/500 [==============================] - 6s 11ms/step - loss: 3.5012 - accuracy: 0.0559
    333/333 - 2s - loss: 3.4943 - accuracy: 0.0562 - 2s/epoch - 7ms/step  
    
#### Discussion: 
    Bad performance.

### Test 2. Using the same structure but without dorpout

#### Result:   
    Epoch 10/10 
    500/500 [==============================] - 6s 11ms/step - loss: 0.4182 - accuracy: 0.8725
    333/333 - 3s - loss: 0.6921 - accuracy: 0.8216 - 3s/epoch - 8ms/step

#### Discussion: 
    It seemed that without dorpout, the performace was improved significantly. 
    However, this might lead to overfitting.

### Test 3. Using the same structure with 20 epochs

#### Result:  
    Epoch 18/20
    500/500 [==============================] - 5s 10ms/step - loss: 3.4918 - accuracy: 0.0590
    Epoch 19/20
    500/500 [==============================] - 6s 12ms/step - loss: 3.4919 - accuracy: 0.0590
    Epoch 20/20
    500/500 [==============================] - 6s 12ms/step - loss: 3.4918 - accuracy: 0.0590
    333/333 - 2s - loss: 3.5073 - accuracy: 0.0523 - 2s/epoch - 5ms/step

    Discussion: 
    Didn't work. After 18 epoch, the accuracy was stucked.

### Test 4. Using different dropout value

#### Result: 

Dorpout: 0.4  

    Epoch 10/10
    500/500 [==============================] - 5s 10ms/step - loss: 3.4918 - accuracy: 0.0565
    333/333 - 2s - loss: 3.5077 - accuracy: 0.0549 - 2s/epoch - 6ms/step

Dorpout: 0.3  

    Epoch 10/10
    500/500 [==============================] - 5s 10ms/step - loss: 2.1570 - accuracy: 0.3306
    333/333 - 2s - loss: 1.6261 - accuracy: 0.4610 - 2s/epoch - 6ms/step

Dorpout: 0.2  

    Epoch 10/10
    500/500 [==============================] - 7s 14ms/step - loss: 0.2722 - accuracy: 0.9276
    333/333 - 2s - loss: 0.3239 - accuracy: 0.9362 - 2s/epoch - 5ms/step

Dorpout: 0.1  

    Epoch 10/10
    500/500 [==============================] - 5s 10ms/step - loss: 0.1754 - accuracy: 0.9571
    333/333 - 2s - loss: 0.3742 - accuracy: 0.9388 - 2s/epoch - 5ms/step

#### Discussion: 
    As the value of dropout decreased, the performance of the model improved. When the dropout was 0.2, 
    the model appeared to achieve a balance between accuracy and not overfitting. 
    However, when runing the model multiple times, its performance was not stable at all.

### Test 5. Add convolutional layer to the CNN structure used the course  
    
Convolutional layer: Conv2D(32, (3, 3), activation='relu', input_shape=(30, 30, 3))  
Max-pooling layer: MaxPooling2D(pool_size=(2, 2))  
Convolutional layer: Conv2D(32, (3, 3), activation='relu')  
Max-pooling layer: MaxPooling2D(pool_size=(2, 2))  
Hidden layer: Dense(128, activation='relu'), with dropout (tf.keras.layers.Dropout(0.5)  
Output layer: Dense(NUM_CATEGORIES, activation='softmax') 

#### Result: 
    Epoch 10/10
    500/500 [==============================] - 7s 13ms/step - loss: 0.2560 - accuracy: 0.9285
    333/333 - 3s - loss: 0.1308 - accuracy: 0.9684 - 3s/epoch - 8ms/step
 
    
#### Discussion: 
    Good and stable performance, not overfitting. I have also tried structures with one max-pooling layer 
    between or after two convolutional layers. Not much difference.

