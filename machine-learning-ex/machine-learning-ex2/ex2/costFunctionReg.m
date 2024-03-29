function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta

hypo = zeros(m, 1);
hypo = sigmoid(X * theta);

for i = 1:m,
    J = J + (1 / m) * ((-y(i)) * log(hypo(i)) - (1 - y(i)) * log(1 - hypo(i)));
end;

J = J + (lambda / (2 * m)) * (sum(theta .^ 2, 1) - theta(1)^2);

temp = ones(size(X));
for i = 1:size(X, 2),
    temp(:, i) = hypo - y;
end;
grad = (1/m) * (sum(temp .* X, 1))';
grad = grad + (lambda / m) * theta;
grad(1) = grad(1) - (lambda / m) * theta(1);

end
