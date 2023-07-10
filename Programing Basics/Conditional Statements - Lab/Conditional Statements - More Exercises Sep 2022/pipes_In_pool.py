v_pool = int(input())
first_pipe_d = int(input())
second_pipe_d = int(input())
time_worker_miss = float(input())

first_pipe_pool_wather = time_worker_miss * first_pipe_d
second_pipe_pool_wather = time_worker_miss * second_pipe_d
wather_amaunt = first_pipe_pool_wather + second_pipe_pool_wather
total_wather_percent = (wather_amaunt / v_pool) * 100
firts_pipe_percent = (first_pipe_pool_wather / wather_amaunt) * 100
second_pipe_percent = (second_pipe_pool_wather / wather_amaunt) * 100
diff = abs(v_pool - wather_amaunt)
if v_pool >= wather_amaunt:
    print(f"f The pool is {total_wather_percent:.2f}% full.Pipe 1: {firts_pipe_percent:.2f}%."
          f"Pipe 2: {second_pipe_percent:.2f}%.")
else:
    print(f"For {time_worker_miss:.2f} hours the pool overflows with {diff:.2f} liters.")
