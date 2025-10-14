# Hint: Manufacturing batches have standardized sizes for quality control
print("Welcome to our quality inspection, for clarification, my inspectors id is: 207705229")

batch_id = input("Enter batch ID: ")

batch_size = int(input("Enter batch size: "))

items = int(input("How many items do you have?: "))

total_quality_score = 0

defect_categories = {
    "none": 0,
    "minor": 0,
    "major": 0
}
# Think: How do you ensure every item in the batch gets inspected?

# Your inspection approach here

for x in range(batch_size):
    print(items, defect_categories)