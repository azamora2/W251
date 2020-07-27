### HW9
### Submission

* How long does it take to complete the training run? (hint: this session is on distributed training, so it *will* take a while)
Approximately 30.5 hours to run 64017 steps.(I went over since I left it running over night and had run our of wifi)
* Do you think your model is fully trained? How can you tell?
No because the eval loss is still decreasing
* Were you overfitting?
yes because the eval loss was greater than the training loss
* Were your GPUs fully utilized?
Yes
![Alt text](https://github.com/azamora2/W251/blob/master/HW9/p100-1.png "p100-1")
![Alt text](https://github.com/azamora2/W251/blob/master/HW9/p100-2.png "p100-2")
* Did you monitor network traffic (hint:  ```apt install nmon ```) ? Was network the bottleneck?
No there was no network bottleneck
![Alt text](https://github.com/azamora2/W251/blob/master/HW9/network1.png "p100-1")
![Alt text](https://github.com/azamora2/W251/blob/master/HW9/network2.png "p100-2")
* Take a look at the plot of the learning rate and then check the config file.  Can you explan this setting?
As expected in training the learning rate increases and subsequently decreases.
* How big was your training set (mb)? How many training lines did it contain?
971 mb and 4.5 million lines.
* What are the files that a TF checkpoint is comprised of?
![Alt text](https://github.com/azamora2/W251/blob/master/HW9/checkpointfiles.png "Checkpoint file")
* How big is your resulting model checkpoint (mb)?
697M
* Remember the definition of a "step". How long did an average step take?
step is epochs divided by batch size. An average step took 0.6 seconds
* How does that correlate with the observed network utilization between nodes?
The longer the steps take the higher the network utilization between the nodes
