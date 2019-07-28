function [J, grad] = costFunction(theta, X, y)
%COSTFUNCTION Compute cost and gradient for logistic regression
%   J = COSTFUNCTION(theta, X, y) computes the cost of using theta as the
%   parameter for logistic regression and the gradient of the cost
%   w.r.t. to the parameters.

% Initialize some useful values
m = length(y); % number of training examples

% return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
%
% Note: grad should have the same dimensions as theta

hypo = zeros(m, 1);
hypo = sigmoid(X * theta);

for i = 1:m,
    J = J + (1 / m) * ((-y(i)) * log(hypo(i)) - (1 - y(i)) * log(1 - hypo(i)));
end;

temp = ones(size(X));
for i = 1:size(X, 2),
    temp(:, i) = hypo - y;
end;
grad = (1/m) * (sum(temp .* X, 1))';

end
