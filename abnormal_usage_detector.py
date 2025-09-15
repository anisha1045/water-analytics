import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

if __name__ == '__main__':
    file_path = 'water_leak_detection_1000_rows.csv'
    num_plots_to_generate = 3

    try:
        # 1. Load the dataset
        data = pd.read_csv(file_path)
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])

        # --- Model Training and Evaluation ---
        features = ['Pressure (bar)', 'Flow Rate (L/s)', 'Temperature (°C)']
        target = 'Leak Status'
        X = data[features]
        y = data[target]

        # Split data for training and testing
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a RandomForestClassifier model
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)

        # Predict on the training data and calculate training accuracy
        y_train_pred = model.predict(X_train)
        training_accuracy = accuracy_score(y_train, y_train_pred)

        # Predict on the testing data and calculate testing accuracy
        y_test_pred = model.predict(X_test)
        testing_accuracy = accuracy_score(y_test, y_test_pred)

        print(f"Training finished.")
        print(f"Training Accuracy: {training_accuracy:.4f}")
        print(f"Testing Accuracy: {testing_accuracy:.4f}")

        # --- Plotting ---
        leaks = data[data['Leak Status'] == 1]
        leak_timestamps = leaks['Timestamp'].tolist()

        # Generate a plot for the first N leaks
        for i, leak_time in enumerate(leak_timestamps[:num_plots_to_generate]):
            plt.figure(figsize=(15, 7))
            plt.plot(data['Timestamp'], data['Flow Rate (L/s)'], label='Flow Rate')
            plt.scatter(leaks['Timestamp'], leaks['Flow Rate (L/s)'], color='red', label='Leak')
            plt.xlabel('Time')
            plt.ylabel('Flow Rate (L/s)')
            plt.title(f'Flow Rate Over Time with Leaks (Zoomed on Leak {i+1})')
            plt.legend()
            plt.grid(True)
            
            # Define a time window around the leak
            start_time = leak_time - pd.Timedelta(minutes=15)
            end_time = leak_time + pd.Timedelta(minutes=15)
            plt.xlim(start_time, end_time)

            plot_filename = f'leak_plot_zoomed_{i+1}.png'
            plt.savefig(plot_filename)
            print(f"\nPlot saved as '{plot_filename}'")

    except FileNotFoundError:
        print(f"Error: '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")