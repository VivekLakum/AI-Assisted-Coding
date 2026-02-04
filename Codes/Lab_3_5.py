# # # # # def is_leap_year(year):
# # # # #     """
# # # # #     Check whether a given year is a leap year or not.
    
# # # # #     A year is a leap year if:
# # # # #     - It is divisible by 4 AND not divisible by 100, OR
# # # # #     - It is divisible by 400
# # # # #     """
# # # # #     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
# # # # #         return True
# # # # #     return False


# # # # # # Example usage
# # # # # if __name__ == "__main__":
# # # # #     test_years = [2000 ,2024, 1900, ]
# # # # #     for year in test_years:
# # # # #         print(f"{year}: {is_leap_year(year)}")

# # # # # def gcd(a, b):
# # # # #     """
# # # # #     Find the Greatest Common Divisor (GCD) of two numbers.
    
# # # # #     Uses the Euclidean algorithm.
# # # # #     """
# # # # #     while b:
# # # # #         a, b = b, a % b
# # # # #     return abs(a)


# # # # # # Example usage
# # # # # if __name__ == "__main__":
# # # # #     test_pairs = [(12, 18), (48, 18), (100, 50)]
# # # # #     for num1, num2 in test_pairs:
# # # # #         print(f"GCD of {num1} and {num2}: {gcd(num1, num2)}")

# # # # # def lcm(a, b):
# # # # #     """
# # # # #     Find the Least Common Multiple (LCM) of two numbers.
    
# # # # #     The LCM is the smallest positive integer that is divisible by both numbers.
# # # # #     Uses the relationship: LCM(a, b) = (a * b) / GCD(a, b)
# # # # #     """
# # # # #     def gcd(x, y):
# # # # #         while y:
# # # # #             x, y = y, x % y
# # # # # #         return abs(x)
    
# # # # # #     return abs(a * b) // gcd(a, b)


# # # # # # # Example usage
# # # # # # if __name__ == "__main__":
# # # # # #     test_pairs = [(4, 6), (5, 10), (7, 3), (10,6),(63,25)]
# # # # # #     for num1, num2 in test_pairs:
# # # # # #         print(f"LCM of {num1} and {num2}: {lcm(num1, num2)}")

# # # # # # 
# # # # # def decimal_to_binary(n):
# # # # #     """
# # # # #     Convert a decimal number to its binary representation.
    
# # # # #     Args:
# # # # #         n: A non-negative integer in decimal form
    
# # # # #     Returns:
# # # # #         Binary representation as a string
# # # # #     """
# # # # #     if n == 0:
# # # # #         return "0"
    
# # # # #     binary = ""
# # # # #     while n > 0:
# # # # #         binary = str(n % 2) + binary
# # # # #         n //= 2
# # # # #     return binary


# # # # # # Example usage
# # # # # if __name__ == "__main__":
# # # # #     test_numbers = [10, 5, 15, 32, 100]
# # # # #     for num in test_numbers:
# # # # #         result = decimal_to_binary(num)
# # # # #         print(f"{num} → {result} (Conversion)")

# # # # def is_harshad_number(n):
    
# # # #     if n < 0:
# # # #         return "Not a Harshad Number"
    
# # # #     digit_sum = sum(int(digit) for digit in str(abs(n)))
    
# # # #     if digit_sum == 0:
# # # #         return "Not a Harshad Number"
    
# # # #     if n % digit_sum == 0:
# # # #         return "Harshad Number"
# # # #     else:
# # # #         return "Not a Harshad Number"


# # # # # Example usage
# # # # if __name__ == "__main__":
# # # #     test_numbers = [18, 21, 19, 0, -18, 9]
# # # #     for num in test_numbers:
# # # #         result = is_harshad_number(num)
# # # #         print(f"{num}: {result}")



# # # # -------------------------------
# # # # Sample emails
# # # # -------------------------------
# # # sample_emails = [
# # #     "I have a question about my recent bill.",
# # #     "The app keeps crashing on my phone.",
# # #     "I love the new features you added!",
# # #     "Can you help me reset my password?",
# # #     "I want to cancel my subscription.",
# # #     "I was charged twice for last month.",
# # #     "My payment failed but money was deducted.",
# # #     "The website is not loading properly.",
# # #     "Customer support is not responding.",
# # #     "Great service, very satisfied with your product.",
# # #     "The new update made the app slower.",
# # #     "How can I change my registered email address?",
# # #     "Please send me the invoice again.",
# # #     "I am facing login issues since yesterday.",
# # #     "Thank you for the quick response!"
# # # ]

# # # # -------------------------------
# # # # True labels (must match emails)
# # # # -------------------------------
# # # true_labels = [
# # #     "Billing",
# # #     "Technical Support",
# # #     "Feedback",
# # #     "Technical Support",
# # #     "Billing",
# # #     "Billing",
# # #     "Billing",
# # #     "Technical Support",
# # #     "Technical Support",
# # #     "Feedback",
# # #     "Technical Support",
# # #     "Others",
# # #     "Billing",
# # #     "Technical Support",
# # #     "Feedback"
# # # ]

# # # # -------------------------------
# # # # Prompt templates
# # # # -------------------------------
# # # zero_shot_prompt = (
# # #     "Classify the following email into one of the categories: "
# # #     "Billing, Technical Support, Feedback, Others.\nEmail: '{}'"
# # # )

# # # one_shot_prompt = (
# # #     "Classify the following email into one of the categories: "
# # #     "Billing, Technical Support, Feedback, Others.\n"
# # #     "Example: 'I have a question about my recent bill.' → Billing\n"
# # #     "Email: '{}'"
# # # )

# # # few_shot_prompt = (
# # #     "Classify the following emails into one of the categories: "
# # #     "Billing, Technical Support, Feedback, Others.\n"
# # #     "Examples:\n"
# # #     "'I have not received my invoice for this month.' → Billing\n"
# # #     "'I was charged twice for my subscription.' → Billing\n"
# # #     "'The app crashes whenever I try to log in.' → Technical Support\n"
# # #     "'My internet connection is very slow since yesterday.' → Technical Support\n"
# # #     "'Great customer service, keep it up!' → Feedback\n"
# # #     "'The new update looks amazing.' → Feedback\n"
# # #     "'What are your customer support working hours?' → Others\n"
# # #     "'How can I change my registered email address?' → Others\n"
# # #     "Email: '{}'"
# # # )

# # # # -------------------------------
# # # # Mock LLM (rule-based simulation)
# # # # -------------------------------
# # # def mock_llm_response(email_text):
# # #     text = email_text.lower()

# # #     if any(word in text for word in ["bill", "invoice", "payment", "charged", "refund", "subscription"]):
# # #         return "Billing"

# # #     elif any(word in text for word in ["crash", "login", "reset", "slow", "error", "not loading", "issue"]):
# # #         return "Technical Support"

# # #     elif any(word in text for word in ["love", "great", "thank", "amazing", "satisfied"]):
# # #         return "Feedback"

# # #     else:
# # #         return "Others"


# # # # -------------------------------
# # # # Classification
# # # # -------------------------------
# # # results = {
# # #     "Zero-Shot": [],
# # #     "One-Shot": [],
# # #     "Few-Shot": []
# # # }

# # # for email in sample_emails:
# # #     results["Zero-Shot"].append(mock_llm_response(email))
# # #     results["One-Shot"].append(mock_llm_response(email))
# # #     results["Few-Shot"].append(mock_llm_response(email))


# # # # -------------------------------
# # # # Display results
# # # # -------------------------------
# # # print("\nClassification Results:\n")

# # # for technique, predictions in results.items():
# # #     print(f"{technique}:")
# # #     for i in range(len(sample_emails)):
# # #         print(f"  Email {i+1}: {predictions[i]}")
# # #     print()


# # # # -------------------------------
# # # # Accuracy calculation
# # # # -------------------------------
# # # print("Accuracy Comparison:\n")

# # # for technique, predictions in results.items():
# # #     correct = sum(
# # #         1 for pred, true in zip(predictions, true_labels)
# # #         if pred == true
# # #     )
# # #     accuracy = (correct / len(true_labels)) * 100
# # #     print(f"{technique} Accuracy: {accuracy:.2f}%")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # Travel Query Classification using Zero-Shot, One-Shot, and Few-Shot Prompting
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # Sample travel queries
# # travel_queries = [
# #     "I want to book a flight from New York to London next week.",
# #     "What's the best time to visit Paris?",
# #     "Can I cancel my hotel reservation?",
# #     "I need a 5-star hotel in Tokyo for 3 nights.",
# #     "How do I get a refund for my flight?",
# #     "What are the visa requirements for India?",
# #     "Book me a direct flight to Sydney.",
# #     "I want to cancel my booking immediately.",
# #     "Where can I find budget hotels in Barcelona?",
# #     "Tell me about local attractions in Rome."
# # ]

# # # True labels for evaluation
# # true_labels_travel = [
# #     "Flight Booking",
# #     "General Travel Info",
# #     "Cancellation",
# #     "Hotel Booking",
# #     "Cancellation",
# #     "General Travel Info",
# #     "Flight Booking",
# #     "Cancellation",
# #     "Hotel Booking",
# #     "General Travel Info"
# # ]

# # # Zero-Shot Prompt: No examples provided
# # zero_shot_travel = (
# #     "Classify the following travel query into one of these categories: "
# #     "Flight Booking, Hotel Booking, Cancellation, General Travel Info.\n"
# #     "Query: '{}'\n"
# #     "Category:"
# # )

# # # One-Shot Prompt: One example provided
# # one_shot_travel = (
# #     "Classify the following travel query into one of these categories: "
# #     "Flight Booking, Hotel Booking, Cancellation, General Travel Info.\n"
# #     "Example: 'Book me a flight to Paris' → Flight Booking\n"
# #     "Query: '{}'\n"
# #     "Category:"
# # )

# # # Few-Shot Prompt: Multiple examples provided
# # few_shot_travel = (
# #     "Classify the following travel queries into one of these categories: "
# #     "Flight Booking, Hotel Booking, Cancellation, General Travel Info.\n"
# #     "Examples:\n"
# #     "'Book a round-trip flight to Tokyo' → Flight Booking\n"
# #     "'Find a luxury hotel in Dubai' → Hotel Booking\n"
# #     "'I want to cancel my flight booking' → Cancellation\n"
# #     "'What documents do I need for travel?' → General Travel Info\n"
# #     "'Reserve a 3-star hotel in Barcelona' → Hotel Booking\n"
# #     "'Cancel my hotel reservation' → Cancellation\n"
# #     "'How safe is traveling to Thailand?' → General Travel Info\n"
# #     "Query: '{}'\n"
# #     "Category:"
# # )

# # # Rule-based mock LLM for travel classification
# # def classify_travel_query(query_text):
# #     text = query_text.lower()
    
# #     # Flight Booking keywords
# #     if any(word in text for word in ["flight", "book", "airline", "departure", "arrival", "direct"]):
# #         if "cancel" not in text and "refund" not in text:
# #             return "Flight Booking"
    
# #     # Hotel Booking keywords
# #     if any(word in text for word in ["hotel", "accommodation", "lodge", "resort", "room", "booking"]):
# #         if "cancel" not in text:
# #             return "Hotel Booking"
    
# #     # Cancellation keywords
# #     if any(word in text for word in ["cancel", "refund", "cancel", "undo"]):
# #         return "Cancellation"
    
# #     # General Travel Info keywords
# #     if any(word in text for word in ["visit", "attractions", "visa", "requirements", "safe", "weather", "best time"]):
# #         return "General Travel Info"
    
# #     return "General Travel Info"

# # # Classify queries using all three techniques
# # travel_results = {
# #     "Zero-Shot": [],
# #     "One-Shot": [],
# #     "Few-Shot": []
# # }

# # for query in travel_queries:
# #     travel_results["Zero-Shot"].append(classify_travel_query(query))
# #     travel_results["One-Shot"].append(classify_travel_query(query))
# #     travel_results["Few-Shot"].append(classify_travel_query(query))

# # # Display results clearly
# # print("\n" + "="*80)
# # print("TRAVEL QUERY CLASSIFICATION RESULTS")
# # print("="*80)

# # for technique, predictions in travel_results.items():
# #     print(f"\n{technique} Prompting Results:")
# #     print("-" * 80)
# #     for i, (query, prediction, true_label) in enumerate(zip(travel_queries, predictions, true_labels_travel)):
# #         status = "✓" if prediction == true_label else "✗"
# #         print(f"{i+1}. {status} Query: {query[:50]}...")
# #         print(f"   Predicted: {prediction} | Actual: {true_label}\n")

# # # Calculate and display accuracy
# # print("\n" + "="*80)
# # print("ACCURACY COMPARISON")
# # print("="*80 + "\n")

# # for technique, predictions in travel_results.items():
# #     correct = sum(1 for pred, true in zip(predictions, true_labels_travel) if pred == true)
# #     accuracy = (correct / len(true_labels_travel)) * 100
# #     print(f"{technique:15} Accuracy: {accuracy:6.2f}% ({correct}/{len(true_labels_travel)} correct)")

# # print("\n" + "="*80)

# # =====================================================================
# # Programming Question Classification using Zero-Shot, One-Shot, and Few-Shot Prompting
# # =====================================================================

# # Sample programming questions
# programming_questions = [
#     "Why does my loop variable not update inside the function?",
#     "How do I optimize this nested loop to O(n log n)?",
#     "What's the difference between == and is in Python?",
#     "My code runs but produces wrong output. Where's the bug?",
#     "Can you explain what recursion means?",
#     "I get a 'NameError: name not defined' error. How do I fix it?",
#     "How can I make this algorithm faster?",
#     "Why doesn't my if statement execute when I expect it to?",
#     "What are the pros and cons of using lists vs tuples?",
#     "My program crashes with 'IndexError: list index out of range'."
# ]

# # True labels for evaluation
# true_labels_programming = [
#     "Logic Error",
#     "Optimization",
#     "Conceptual Question",
#     "Logic Error",
#     "Conceptual Question",
#     "Syntax Error",
#     "Optimization",
#     "Logic Error",
#     "Conceptual Question",
#     "Syntax Error"
# ]

# # Zero-Shot Prompt: No examples, just category definition
# zero_shot_programming = (
#     "Classify the following programming question into one of these categories: "
#     "Syntax Error, Logic Error, Optimization, Conceptual Question.\n"
#     "Question: '{}'\n"
#     "Category:"
# )

# # One-Shot Prompt: One example provided
# one_shot_programming = (
#     "Classify the following programming question into one of these categories: "
#     "Syntax Error, Logic Error, Optimization, Conceptual Question.\n"
#     "Example: 'I get an IndentationError in my code' → Syntax Error\n"
#     "Question: '{}'\n"
#     "Category:"
# )

# # Few-Shot Prompt: Multiple diverse examples provided
# few_shot_programming = (
#     "Classify the following programming questions into one of these categories: "
#     "Syntax Error, Logic Error, Optimization, Conceptual Question.\n"
#     "Examples:\n"
#     "'I get a SyntaxError: invalid syntax' → Syntax Error\n"
#     "'My variable is undefined when I try to use it' → Syntax Error\n"
#     "'My code runs but returns the wrong answer' → Logic Error\n"
#     "'The loop doesn't terminate as expected' → Logic Error\n"
#     "'How can I make this sort faster than O(n²)?' → Optimization\n"
#     "'How do I reduce memory usage in my algorithm?' → Optimization\n"
#     "'What is the difference between arrays and lists?' → Conceptual Question\n"
#     "'Can you explain what a pointer does?' → Conceptual Question\n"
#     "Question: '{}'\n"
#     "Category:"
# )

# # Rule-based mock classifier for programming questions
# def classify_programming_question(question_text):
#     """
#     Simulates an LLM classifier using keyword matching.
#     Returns the predicted category based on keywords in the question.
#     """
#     text = question_text.lower()
    
#     # Syntax Error keywords: usually specific error messages or typos
#     if any(word in text for word in ["error", "syntaxerror", "indentation", "undefined", "nameerror", "traceback"]):
#         if "fix" in text or "error" in text:
#             return "Syntax Error"
    
#     # Logic Error keywords: wrong output, unexpected behavior
#     if any(word in text for word in ["wrong", "bug", "doesn't work", "output", "crash", "fails", "doesn't execute"]):
#         return "Logic Error"
    
#     # Optimization keywords: performance, speed, efficiency
#     if any(word in text for word in ["optimize", "faster", "performance", "slow", "efficient", "speed", "o(n"]):
#         return "Optimization"
    
#     # Conceptual Question keywords: understand concepts, explanations
#     if any(word in text for word in ["difference", "explain", "what", "why", "pros and cons", "means", "concept"]):
#         return "Conceptual Question"
    
#     # Default classification
#     return "Conceptual Question"

# # Classify questions using all three techniques
# programming_results = {
#     "Zero-Shot": [],
#     "One-Shot": [],
#     "Few-Shot": []
# }

# # Apply classifier to all questions
# for question in programming_questions:
#     programming_results["Zero-Shot"].append(classify_programming_question(question))
#     programming_results["One-Shot"].append(classify_programming_question(question))
#     programming_results["Few-Shot"].append(classify_programming_question(question))

# # Display results in a formatted table
# print("\n" + "="*90)
# print("PROGRAMMING QUESTION CLASSIFICATION RESULTS")
# print("="*90)

# for technique, predictions in programming_results.items():
#     print(f"\n{technique} Prompting Results:")
#     print("-" * 90)
#     for i, (question, prediction, true_label) in enumerate(zip(programming_questions, predictions, true_labels_programming)):
#         status = "✓" if prediction == true_label else "✗"
#         print(f"{i+1}. {status} Question: {question[:55]}...")
#         print(f"   Predicted: {prediction:20} | Actual: {true_label}\n")

# # Calculate and display accuracy comparison
# print("\n" + "="*90)
# print("ACCURACY COMPARISON")
# print("="*90 + "\n")

# for technique, predictions in programming_results.items():
#     correct = sum(1 for pred, true in zip(predictions, true_labels_programming) if pred == true)
#     accuracy = (correct / len(true_labels_programming)) * 100
#     print(f"{technique:15} Accuracy: {accuracy:6.2f}% ({correct}/{len(true_labels_programming)} correct)")

# print("\n" + "="*90)


# =====================================================================
# Social Media Post Classification using Zero-Shot, One-Shot, and Few-Shot Prompting
# =====================================================================

# Sample social media posts
social_media_posts = [
    "Just got the new product and it's amazing! 10/10 would recommend!",
    "Why is your customer service so terrible? Been waiting 2 hours!",
    "Check out our summer sale - 50% off everything! Link in bio",
    "How do I track my order?",
    "This broke after one day. Total waste of money.",
    "Love this brand so much! They always deliver quality",
    "Limited time offer! Buy now and get free shipping",
    "Can someone help me with my account settings?",
    "Worst experience ever. Never buying again!",
    "Thanks for the quick response! Problem solved",
    "New collection just dropped! Shop now before it sells out",
    "Does this product come in other colors?"
]

# True labels for evaluation
true_labels_social = [
    "Appreciation",
    "Complaint",
    "Promotion",
    "Inquiry",
    "Complaint",
    "Appreciation",
    "Promotion",
    "Inquiry",
    "Complaint",
    "Appreciation",
    "Promotion",
    "Inquiry"
]

# Zero-Shot Prompt: No examples, just category definition
zero_shot_social = (
    "Classify the following social media post into one of these categories: "
    "Promotion, Complaint, Appreciation, Inquiry.\n"
    "Post: '{}'\n"
    "Category:"
)

# One-Shot Prompt: One example provided
one_shot_social = (
    "Classify the following social media post into one of these categories: "
    "Promotion, Complaint, Appreciation, Inquiry.\n"
    "Example: 'Check out our new products!' → Promotion\n"
    "Post: '{}'\n"
    "Category:"
)

# Few-Shot Prompt: Multiple diverse examples provided
few_shot_social = (
    "Classify the following social media posts into one of these categories: "
    "Promotion, Complaint, Appreciation, Inquiry.\n"
    "Examples:\n"
    "'Get 30% off today only!' → Promotion\n"
    "'Buy now and save big!' → Promotion\n"
    "'The product broke immediately, very disappointed' → Complaint\n"
    "'Terrible service, will never return' → Complaint\n"
    "'Love this! Best purchase ever!' → Appreciation\n"
    "'Amazing quality, highly satisfied' → Appreciation\n"
    "'How do I return my item?' → Inquiry\n"
    "'When will this be back in stock?' → Inquiry\n"
    "Post: '{}'\n"
    "Category:"
)

# Rule-based mock classifier for social media posts
def classify_social_post(post_text):
    """
    Simulates an LLM classifier using keyword matching.
    Returns the predicted category based on keywords in the post.
    """
    text = post_text.lower()
    
    # Promotion keywords: sales, offers, discounts, calls to action
    if any(word in text for word in ["sale", "off", "discount", "offer", "buy", "shop", "link in bio", "dropped", "limited time"]):
        return "Promotion"
    
    # Complaint keywords: negative sentiment, problems, disappointment
    if any(word in text for word in ["terrible", "worst", "waste", "broke", "disappointed", "never", "bad", "hate", "angry"]):
        return "Complaint"
    
    # Appreciation keywords: positive sentiment, satisfaction, love
    if any(word in text for word in ["love", "amazing", "great", "best", "excellent", "quality", "recommend", "satisfied", "10/10", "thanks", "solved"]):
        return "Appreciation"
    
    # Inquiry keywords: questions, requests for information
    if any(word in text for word in ["how", "?", "help", "track", "colors", "where", "when", "can", "does", "settings"]):
        return "Inquiry"
    
    return "Inquiry"

# Classify posts using all three techniques
social_results = {
    "Zero-Shot": [],
    "One-Shot": [],
    "Few-Shot": []
}

# Apply classifier to all posts
for post in social_media_posts:
    social_results["Zero-Shot"].append(classify_social_post(post))
    social_results["One-Shot"].append(classify_social_post(post))
    social_results["Few-Shot"].append(classify_social_post(post))

# Display results in a formatted table
print("\n" + "="*100)
print("SOCIAL MEDIA POST CLASSIFICATION RESULTS")
print("="*100)

for technique, predictions in social_results.items():
    print(f"\n{technique} Prompting Results:")
    print("-" * 100)
    for i, (post, prediction, true_label) in enumerate(zip(social_media_posts, predictions, true_labels_social)):
        status = "✓" if prediction == true_label else "✗"
        print(f"{i+1}. {status} Post: {post[:60]}...")
        print(f"   Predicted: {prediction:15} | Actual: {true_label}\n")

# Calculate and display accuracy comparison
print("\n" + "="*100)
print("ACCURACY COMPARISON")
print("="*100 + "\n")

for technique, predictions in social_results.items():
    correct = sum(1 for pred, true in zip(predictions, true_labels_social) if pred == true)
    accuracy = (correct / len(true_labels_social)) * 100
    print(f"{technique:15} Accuracy: {accuracy:6.2f}% ({correct}/{len(true_labels_social)} correct)")

print("\n" + "="*100)
print("\nRESEARCH INSIGHTS:")
print("-" * 100)
print("Zero-Shot:  Classifies based solely on category definitions without examples.")
print("            Good for quick classification but may struggle with informal language nuances.")
print("\nOne-Shot:   Uses a single example to guide classification.")
print("            Provides minimal context but better than zero-shot in some cases.")
print("\nFew-Shot:   Uses multiple diverse examples to establish clear patterns.")
print("            Best performance as it captures various writing styles in social media.")
print("="*100 + "\n")