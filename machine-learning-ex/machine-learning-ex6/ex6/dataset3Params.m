function [C, sigma] = dataset3Params(X, y, Xval, yval)
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = DATASET3PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

minmean = 100000000;
mini = 0.01;
minj = 0.01;

for i = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30],
    for j = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30],
        model = svmTrain(X, y, i, @(x1, x2) gaussianKernel(x1, x2, j));
        pred = svmPredict(model, Xval);
        tempmean = mean(double(pred ~= yval));
        if tempmean < minmean,
            minmean = tempmean;
            mini = i;
            minj = j;
        end;
    end;
end;

C = mini;
sigma = minj;

end
