from scipy import stats

def perform_hypothesis_test(sample1, sample2):
    t_statistic, p_value = stats.ttest_ind(sample1, sample2)
    return p_value

# Example usage:
sample1 = list(map(int,input("Enter the list 1 elements : ").split()))
sample2 = list(map(int,input("Enter the list 2 elements : ").split()))
print(sample1, sample2)
p_value = perform_hypothesis_test(sample1, sample2)
print("P-value : ", p_value)