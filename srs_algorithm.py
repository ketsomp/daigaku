"""
Spaced Repetition System (SRS) Algorithm implementation.
Based on the SM-2 algorithm (SuperMemo 2).
"""
from datetime import datetime, timedelta


class SRSAlgorithm:
    """
    Implements the Spaced Repetition System for flashcard scheduling.
    """
    
    @staticmethod
    def calculate_next_review_interval(answer_quality, repetition_count=0, previous_interval=1):
        """
        Calculate the next review interval based on answer quality.
        
        Args:
            answer_quality (int): Quality of answer (1-5)
                1: Complete blackout
                2: Incorrect, but recognized
                3: Correct with difficulty
                4: Correct with hesitation
                5: Perfect recall
            repetition_count (int): Number of successful repetitions
            previous_interval (int): Previous interval in days
        
        Returns:
            tuple: (next_interval_days, new_repetition_count)
        """
        if answer_quality < 3:
            # Reset if answer was poor
            return (1, 0)
        
        if repetition_count == 0:
            interval = 1
        elif repetition_count == 1:
            interval = 6
        else:
            # Calculate ease factor (EF)
            ease_factor = 1.3 + (answer_quality - 3) * 0.1
            interval = int(previous_interval * ease_factor)
        
        return (interval, repetition_count + 1)
    
    @staticmethod
    def is_card_due(last_review_date, interval_days):
        """
        Check if a card is due for review.
        
        Args:
            last_review_date (datetime): Date of last review
            interval_days (int): Interval in days before next review
        
        Returns:
            bool: True if card is due for review
        """
        if last_review_date is None:
            return True
        
        next_review_date = last_review_date + timedelta(days=interval_days)
        return datetime.now().date() >= next_review_date.date()
    
    @staticmethod
    def get_card_priority(last_review_date, answer_quality):
        """
        Calculate priority score for card review order.
        Lower score = higher priority.
        
        Args:
            last_review_date (datetime): Date of last review
            answer_quality (int): Last answer quality (1-5)
        
        Returns:
            float: Priority score
        """
        if last_review_date is None:
            return 0  # Highest priority for new cards
        
        days_since_review = (datetime.now().date() - last_review_date.date()).days
        quality_factor = 6 - answer_quality  # Lower quality = higher priority
        
        return days_since_review + (quality_factor * 2)
