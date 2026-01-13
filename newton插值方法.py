%sqrt(x)
插值
clear;
clc;
xlist = [100, 121, 144];
ylist = [10, 11, 12];
x = 115;

%牛顿插值

[p, q] = getDQ(xlist, ylist);
yN = q(1) + q(2) * (x - x0) + q(3) * (x - x0) * (x - x1);
fprintf('sqrt(115)牛顿插值的结果为：%.6f\n', yN)

%计算差商
function[p, q] = getDQ(x, y)
%x
为节点，y
为函数值, 向量
x
与向量
y
的长度必须一致
%p
是差商表
%q
为差商表中对角线的值

m = length(x);
x = x(:); p = zeros(m, m + 1);
p(:, 1) = x;
p(:, 2) = y(:);
for k = 3: m + 1
p(k - 1: m, k) = diff(p(k - 2: m, k - 1))./ (x(k - 1:m) - x(1: m + 2 - k) );
end
q = diag(p(1:m, 2: m + 1));
end 
