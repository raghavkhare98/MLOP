"""
Q1. You're evaluating a classification model with a precision of 0.8 and a recall of 0.75. How 
would you compute and interpret the F1 score in this scenario, and what insights can you 
draw about the model's overall performance in balancing precision and recall
"""

q1_precision = 0.8
q1_recall = 0.75

q1_f1_score = 2 * ((q1_precision * q1_recall)/ (q1_precision + q1_recall))
q1_interpretation = "since the precision is higher than recall, our model can perform better at avoiding false positives. However, even though recall is not too low, but if false negatives are crucial, then we should work upon increasing the recall. The F1 score shows a good balance between precision and recall. The f1 score comes out to be 0.77 which shows that the model has a good balance between detecting false positives and false negatives"
print(f"F1 score for question 1 is: {q1_f1_score:.2f}.\n My interpretation of these scores is that, {q1_interpretation}\v")

"""
Q2. In a different classification context, suppose the precision of a model is measured at 0.85 
while its recall is 0.9. How does the computation of the F1 score capture the trade-off 
between precision and recall, and what implications does the resulting score hold for 
assessing the model's effectiveness?
"""

q2_precision = 0.85
q2_recall = 0.9

q2_interpretation = "the model performs better at finding false negatives(due to the recall being 0.9), as compared to the false positives(0.85). Since both precisiona and recall are high, the model has a really good F1 score of 0.87 which means that it's predictions are highly accurate, with a better performace leaning towards finding false negatives, which is useful where we want false negatives to be very low"
q2_f1_score = 2 * ((q2_precision * q2_recall) / (q2_precision + q2_recall))
print(f"F1 score for question 2 is: {q2_f1_score:.2f}.\n My interpretation of these scores is that, {q2_interpretation}\v")

"""
Q3. You encounter a classification scenario where the precision of a model is 0.7 and its recall is 
0.8. How would you calculate the F1 score, and what strategic considerations should be 
taken into account when interpreting this metric to inform decision-making?
"""

q3_precision = 0.7
q3_recall = 0.8

q3_interpretation = "the recall is higher(0.8) than precision(0.7), hence the model's f1 score is decreased at around 0.75. This means that the model's predictions would be somewhat accurate with false negatives being more correct as opposed to false positives due to the low precision value. The precision value is quite lower at 0.7 and hence, there's room for improvements to increase the F1 score and achieving better predicability"
q3_f1_score = 2 * ((q3_precision * q3_recall) / (q3_precision + q3_recall))
print(f"F1 score for question 3 is: {q3_f1_score:.2f}.\n My interpretation of these scores is that, {q3_interpretation}\v")

"""
Q4. Suppose a classification model achieves a precision of 0.9 and a recall of 0.85. How does the 
F1 score encapsulate the model's performance in terms of both precision and recall, and 
what actionable insights can be derived from this comprehensive evaluation?
"""

q4_precision = 0.9
q4_recall = 0.85

q4_interpretation = "The F1 score is 0.87 which says that the model performs really well in prediction, but from the precision value that the accuracy of predicting a false positive is higher as opposed to a false negative which is shown by recall's value of 0.85. This model would perform well in the scenarios where the detection false positives are more critical as opposed to false negatives"
q4_f1_score = 2 * ((q4_precision * q4_recall) / (q4_precision + q4_recall))
print(f"F1 score for question 4 is: {q4_f1_score:.2f}.\n My interpretation of these scores is that, {q4_interpretation}\v")

"""
Q5. You're assessing a classifier with a precision of 0.75 and a recall of 0.7. How does the F1 
score offer a balanced assessment of the model's performance, and what implications does it 
hold for optimizing model parameters or refining the classification process?
"""

q5_precision = 0.75
q5_recall = 0.7

q5_interpretation = "The model's f1 score is 0.72 which is fairly low, and hence the model would work just fine, with the detection of false posivites slightly accurate(precision is 0.75) than false negatives(as recall is just 0.7). The model is not that accurate in predicatbility but still, can perform better in predicting false positives due to a higher precision score"
q5_f1_score = 2 * ((q5_precision * q5_recall) / (q5_precision + q5_recall))
print(f"F1 score for question 5 is: {q5_f1_score:.2f}.\n My interpretation of these scores is that, {q5_interpretation}\v")

"""
Q6. In a classification scenario where the precision is 0.65 and the recall is 0.75, how would you 
compute and interpret the F1 score? Additionally, what strategic adjustments might be made 
based on the insights provided by this metric?
"""

q6_precision = 0.65
q6_recall = 0.75
q6_interpretation = "The model's precision is quite low and needs to be re-trained. Due to the precision being very low, the model would be more prone to false posivtives and, although should not be used for any tasks, but it would be a very bad choice for tasks which depend on a higher true positive count. Recall is also low but still compartively better than the precision, hence the model would be a little bit better in detecting false negatives, though it is still bad, which decreases the F1 score of the model"
q6_f1_score = 2 * ((q6_precision * q6_recall) / (q6_precision + q6_recall))
print(f"F1 score for question 6 is: {q6_f1_score:.2f}.\n My interpretation of these scores is that, {q6_interpretation}\v")

"""
Q7. Suppose a classification model achieves a precision of 0.8 and a recall of 0.85. How does the 
F1 score capture the model's performance in terms of both false positives and false 
negatives, and how might this information guide further model refinement or optimization?
"""

q7_precision = 0.8
q7_recall = 0.85
q7_interpretation = "The model's precision and recall scores are good with the recall score being slightly better than the precision score, and hence the model would perform well in tasks which require for false negative predictions to be less. The F1 score of this model would be pretty high, and it would predict false negatives better than false positives. Further optimization can be made in the recall score to make very strong predictions for recall values by training the model on more values of the false negatives class"

q7_f1_score = 2 * ((q7_precision * q7_recall) / (q7_precision + q7_recall))
print(f"F1 score for question 7 is: {q7_f1_score:.2f}.\n My interpretation of these scores is that, {q7_interpretation}\v")

"""
Q8. You're evaluating a classifier with a precision and recall both measured at 0.9. How does the 
computation of the F1 score reflect the model's ability to achieve a balance between 
precision and recall, and what implications does this balanced evaluation hold for practical 
applications? 
"""

q8_precision = 0.9
q8_recall = 0.9
q8_interpretation = "The model's F1 score would be very high leading to very accurate predictions across all classes (flase positives and negatives). Due to both the recall and precision being high, the model is an excellent choice where making predictions free of any false predictions is crucial (like a medical prediction scenario)."

q8_f1_score = 2 * ((q8_precision * q8_recall) / (q8_precision + q8_recall))
print(f"F1 score for question 8 is: {q8_f1_score:.2f}.\n My interpretation of these scores is that, {q8_interpretation}\v")

"""
Q9. In a classification context where the precision is 0.95 and the recall is 0.9, how would you 
calculate the F1 score, and what strategic considerations should be taken into account when 
interpreting this metric to inform decision-making?
"""

q9_precision = 0.95
q9_recall = 0.9
q9_interpretation = "The F1 score of this model would be extremely high due to which the model is almost unmatched in terms of predictions. Since it's precision value is slightly higher than the recall value, the model would perform quite well in scenarios where we want lesser false positives, but that being said, the model would be very accurate in predicting false negatives too because it's recall value is 0.9 and the overall prediction quotient would be very high too given it's impressive F1 score"

q9_f1_score = 2 * ((q9_precision * q9_recall) / (q9_precision + q9_recall))
print(f"F1 score for question 9 is: {q9_f1_score:.2f}.\n My interpretation of these scores is that, {q9_interpretation}\v")

"""
Q10. Suppose a classification model achieves a precision of 0.85 and a recall of 0.95. How does the 
F1 score provide a comprehensive evaluation of the model's performance, and what insights 
can be derived to optimize both precision and recall simultaneously?
"""

q10_precision = 0.85
q10_recall = 0.95
q10_interpretation = "The F1 score would be very high leading to highly accurate predictions. From the recall and prediction values (0.95 and 0.85 respectively), I can derive that the model would have an extremely low number of false negative predictions, susceptible to only outliers. But still, the false positives would be very low too (though not as low as the false negatives) because of it's very impressive precision score. Overall, with the F1 score being high, I can confidently say that this model is good at predictions"

q10_f1_score = 2 * ((q10_precision * q10_recall) / (q10_precision + q10_recall))
print(f"F1 score for question 10 is: {q10_f1_score:.2f}.\n My interpretation of these scores is that, {q10_interpretation}\v")