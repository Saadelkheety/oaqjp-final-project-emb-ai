import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        text_to_analyse = "I am glad this happened"
        self.assertEqual(emotion_detector(text_to_analyse).get('dominant_emotion'), 'joy')
        text_to_analyse = "I am really mad about this"
        self.assertEqual(emotion_detector(text_to_analyse).get('dominant_emotion'), 'anger')
        text_to_analyse = "I feel disgusted just hearing about this"
        self.assertEqual(emotion_detector(text_to_analyse).get('dominant_emotion'), 'disgust')
        text_to_analyse = "I am so sad about this"
        self.assertEqual(emotion_detector(text_to_analyse).get('dominant_emotion'), 'sadness')
        text_to_analyse = "I am really afraid that this will happen"
        self.assertEqual(emotion_detector(text_to_analyse).get('dominant_emotion'), 'fear')


if __name__ == '__main__':
    unittest.main()