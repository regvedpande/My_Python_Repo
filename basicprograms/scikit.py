from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Sample data: area (sq.ft), bedrooms, and price (in lakhs)
X = [[1200, 3], [1500, 4], [900, 2], [1100, 2], [1300, 3]]
y = [75, 100, 60, 65, 80]

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Actual:", y_test)
