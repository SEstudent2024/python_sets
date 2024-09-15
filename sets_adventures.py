# 1. Python Sets Adventure
# Objective: The aim of this assignment is to deepen your understanding and application of Python sets.

# Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

# Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}


# 1. Destinations that both airlines fly to 
shared_destinations = our_routes & competitor_routes

# 2. Destinations unique to your airline 
unique_to_our_airline = our_routes - competitor_routes

# 3. Destinations that neither airline shares
unique_to_both = our_routes ^ competitor_routes

# Output the results
print("Destinations both airlines fly to:", shared_destinations)
print("Destinations unique to our airline:", unique_to_our_airline)
print("Destinations that neither airline shares:", unique_to_both)