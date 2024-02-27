import numpy as np
x1 = np.random.randint(100, size = 100)
x2 = np.random.randint(200, size = 100)
y = 3 * x1 + 2 * x2 - 1
x1 = x1 + np.random.randint(5, size = 100) / 10
x2 = x2 + np.random.randint(5, size = 100) / 10
y = y + np.random.randint(5, size = 100) / 10
lrs = [0.00005, 0.00001, 0.00002, 0.00003, 0.00004]
epochs_range = [120, 400, 350]
best_lr = None
best_loss = float('inf')
best_epoch = None
for lr in lrs:
  for epoch in epochs_range:
    w1 = 0
    w2 = 0
    w0 = 0
    for in_one_epoch in range(1, epoch + 1):
      for i in range(len(x1)):
        pred = w1 * x1[i] + w2 * x2[i] + w0
        w1 += 2 * lr * x1[i] * (y[i] - pred)
        w2 += 2 * lr * x2[i] * (y[i] - pred)
        w0 += 2 * lr * (y[i] - pred)
      loss = 0
    for j in range(len(x1)):
      loss += 1 / len(x1) * (y[i] - (w1 * x1[i] + w2 * x2[i] + w0))**2
    if loss < best_loss:
      best_loss = loss
      best_lr = lr
      best_epoch = epoch
#прогонка с наилучшими весами (веса не просто последние получившиеся)
w1 = 0
w2 = 0
w0 = 0
for e in range(1, best_epoch + 1):
  for k in range(len(x1)):
    pred = w1 * x1[i] + w2 * x2[i] + w0
    w1 += 2 * best_lr * x1[i] * (y[i] - pred)
    w2 += 2 * best_lr * x2[i] * (y[i] - pred)
    w0 += 2 * best_lr * (y[i] - pred)
print('best loss:', best_loss)
print('best lr:', best_lr)
print('best epoch:', epoch)
print(f'w1 = {w1}, w2 = {w2}, w0 = {w0}')
#результаты постоянно меняются, на одинаковом количестве эпох могут как попасться хорошие веса, так и нет.
#lr работает только в этом диапозоне - если больше, то ошибка
#не знаю как решить, но может так и должно быть: лучшим количеством эпох всегда является последнее в списке количества эпох, хотя, вроде как, лучшему количеству должно присваиваться значение с наименьшим лоссом, а не факт, что у последнего он наименьший
