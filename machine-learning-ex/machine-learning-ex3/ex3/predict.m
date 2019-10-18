function p = predict(Theta1, Theta2, X)
%PREDICT Predict the label of an input given a trained neural network
%   p = PREDICT(Theta1, Theta2, X) outputs the predicted label of X given the
%   trained weights of a neural network (Theta1, Theta2)

% Useful values
m = size(X, 1);
num_labels = size(Theta2, 1);

% You need to return the following variables correctly 
p = zeros(size(X, 1), 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Complete the following code to make predictions using
%               your learned neural network. You should set p to a 
%               vector containing labels between 1 to num_labels.

A1 = [ones(m, 1), X];
Z2 = Theta1 * A1';
A2 = sigmoid(Z2);
A2 = [ones(1, m); A2];
Z3 = Theta2 * A2;
hypo = sigmoid(Z3);
[val, ind] = max(hypo, [], 1);
p = ind(:);

end
