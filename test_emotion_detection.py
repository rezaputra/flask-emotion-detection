import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detection(self):
        tests = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear")
        ]

        for statement, expected_emotion in tests:
            with self.subTest(statement=statement):
                result = emotion_detector(statement)
                dominant_emotion = result['dominant_emotion'].lower()
                self.assertEqual(dominant_emotion, expected_emotion,
                                 f"Expected emotion for '{statement}' should be '{expected_emotion}'")

if __name__ == '__main__':
    unittest.main()
