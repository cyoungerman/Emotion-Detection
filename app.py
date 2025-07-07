from emotion_detection import emotion_detector

def main():
    # Sample text to analyze
    sample_text = "I am so happy I am doing this"

    # Call the emotion detection function
    result = emotion_detector(sample_text)

    # Display the result
    print("Emotion Detection Result:")
    print(result)

if __name__ == "__main__":
    main()


