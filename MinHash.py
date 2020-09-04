
# The steps required for this program are#
# 1. Convert each test file into a set of shingles.
#    - Form shingles by taking 3 words together.
#    - Encode shingles to 32 bit integers. (Can use a CRC32 hash for this)
# 2. Compute all Jaccard similarities.
# 3. Compute the MinHash signature for each document.
#    - Use the Fast MinHash algorithm as dicussed in class so that explicit 
#      permutations of all shingle IDs are not required.
# 4. Compare MinHash signatures to one another for finding plagiarism.
#    - Compare the MinHash signatures by finding out the number of components in which
#      the signatures are equal and taking a average of them.
#    - Show the pairs of documents where similarity is greater than 0.5.

import os
import re
import random
import time
import binascii

# Set the number of rows (or components) in the MinHash signatures. Will also need this
# many hash functions.
numHashRows = 10;

# Now run the MinHash algorithm for different portions of the dataset. /data directory has
# different data files with 100, 1000, and 10,000 documents.

numDocs = 100 # Start with 100. Meaning there are 100 articles in 1 data file (same as 100 individual docs).
dataFile = "./data/docs_" + str(numDocs) + ".train"
plagFile = "./data/docs_" + str(numDocs) + ".plag"

# Create ground truths from the plagiarism results already provided.
# They will be useful later on for checking true and false positives.

plagiarisms = {}

# Open the plag file.
f = open(plagFile, "rU")

# For each pair reported
for line in f:
  
  # Remove new-line character if present
  if line[-1] == '\n':
      line = line[0:-1]
      
  docs = line.split(" ")

  # Keep a map of the two documents
  plagiarisms[docs[0]] = docs[1]
  plagiarisms[docs[1]] = docs[0]

# Now convert the documents to shingles

print "Creating Shingles..."

# Keep a current ID for the current shingle. When a new shingle is encountered in
# the dictionary, we will update this.

currentShingleID = 0

# Create a dictionary for the articles having a mapping of the article identifier
# for example t123, to the list of the shingle IDs.

documentShingleSets = {};
  
# Open the data file.
f = open(dataFile, "rU")

documentNames = []

numShingles = 0

for i in range(0, numDocs):

  # ADD CODE HERE TO DO THE FOLLOWING:

  # Read akk the words (may need splitting)
  # Maintain a list of document IDs (article IDs)

  # Create a set of shingles called shinglesInDocument

  # For each word in document create a shingle by combining 3 consecutive
  # words together. This is where the Python set will help as it will 
  # automatically remove duplicate shingles.

  # Use the binascii library to hash every shingle to a 32 bit integer.
  # Read binascii manual to find out how to use them.
  # Add the hashed value to the set.

  # Now add the completed set of shingles to the documentShingleSets dictionary.
  # Keep a count of the total number of shingles found in numShingles.

# Close the data file.  
f.close()  

print '\nAverage shingles per document: %.2f' % (numShingles / numDocs)

# Now we are going to compute the similarity values. For that we need to store the
# values in a matrix which you know will be sparse. So, we are going to store it
# in the conventional matrix way (using a row0major implementation).

# Second optimized way is to use a triangular matrix as it consumes only half of
# size of a full matrix. BONUS POINTS IF YOU DO THIS.

#Find out how many elements you will need
totalSize = int(numDocs * (numDocs - 1) / 2)

# Now intiialize two lists to store 2 similarity values. 
# 1. JaccSim to store the Jaccard Similarity
# 2. MinHashSim will be the estimated similarity by comparing the MinHash signatures.

JaccSim = [0 for x in range(numElems)]
MinHashSim = [0 for x in range(numElems)]

# Define a function to map a 2D matrix co-ordinate to a 1D index.
# If you use triangular matrix, then this logic will change. The idea
# is explained in MMDS book Chap 6.

def getMatrixIndex(i, j):
    #ADD YOUR CODE HERE

    return k


# ONE COMPARISON WILL BE TO STUDY HOW MUCH JACCARD SIMILARITY IS SLOWER THAN
# COMPUTING MIN HASH. INSERT TIMERS TO DO A COMPARISON

print "\nCalculating Jaccard Similarities..."


# For every document pair...
    for i in range(0, numDocs):
      

      # Get shingle set for document i 
      for j in range(i + 1, numDocs):
          # Get shingle set for document j

          #Calculate and store the Jaccard Similarities

          JaccSim[getMatrixIndex(i, j)] = # ADD YOUR CODE


# May need to delete JaccSim as it can be a very big matrix. Especially for larger 
# document sizes.
# del JaccSim
        

# Now perform Min Hashing. AGAIN YOU CAN INSERT TIMERS TO FIND OUT THE SPEED DIFFERENCE
# WITH JACC SIM.

print '\nGenerate random hash functions...'

# Store the maximum shingle ID
maximumShingleID = # ADD CODE

# FOR HASH FUNCTIONS IT IS BETTER TO USE PRIME NUMBERS.
# THIS WILL BE SIMILAR TO SETTING UP THE INFINITY VALUE OF THE LARGEST POSSIBLE HASH.
# ALSO THIS WILL REDUCE POSSIBLE COLLISIONS.
# YOU CAN FIND A PRIME NUMBER GREATER THAN maximumShingleID at the following URL.
# http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php

oneLargePrime = # LOOK UP AND ADD


# The hash function we will use will be of the following form:
#   h(x) = (a*x + b) % c
# Where 'x' is the input value, 'a' and 'b' are random coefficients, and 'c' is
# a prime number just greater than maximumShingleID.

# Now generate a list of 'k' random coefficients while also ensuring that the
# random number you pick for 'a' and 'b' is unique.

def generateRandomCoeeficients(k):
    #List of k random coefficients
    randomCoeffList = []
  
    # ADD CODE TO FILL UP randomCoeffList

  return randomCoeffList

# For the 'numhashRows' number of hash functions, pick different 'a' and 'b'

coefficientsA = generateRandomCoefficients(numHashRows)
coefficientsB= generateRandomCoefficients(numHashRows)

print '\nComputing MinHash signatures for all documents...'

# Create a list of documents as signature vectors
signatures = []

# Now write the code for the Fast MinHash algorithm. Rather than finding the random
# permutations of all shingles, just find out the hashes for the IDs that are 
# actually present in the document. Then take the lowest hash code value. This will
# be the index of the first shingle that you will encounter in the randomized order.
# For each document...

for documentID in documentNames:
  # ADD CODE FOR FOLLOWING:
  # Get the shingle set for the current document.
  # Initialize an empty signature vector 'sign'
  # Start loop over all hash functions 'numHashRows'
       # For every ith hash function, find it's hash code.
       # For every shingle in the document
           # Using the h(x) function. 'a' and 'b' values already populated
           # Take c as 'largePrime'
           # Keep track the lowest hash code.
       # Append the smallest hash code seen in 'sign'
  # Append the computed vector to 'signatures'



# NOW COMPARE THE MINHASH VALUES FOR ALL DOCUMENTS

# ADD CODE FOR FOLLOWING:
# For all the documents
    # Get signature for 'ith' document
    # For every other document
        # Count the number of positions in the minhash signature where they are equal.
    # Record the average number of positions in which they matched and store in 'MinHashSim'.
   
    
# Now display similar document pairs
# Initialize variables for true positives and false positives.

tp = 0
fp = 0
  
# SET THRESHOLD
threshold = 0.5

# ADD CODE FOR FOLLOWING

# FOR i in 0 to ALL DOCUMENTS
    # FOR j in i+1 to ALL DOCUMENTS
        # Get JaccSim of the pair (i,j)
        # Get MinHashSim for the pair (i, j)
        # Print both
        # find out by comparing with ground truth if it is a true positive
        # or a false positive. Display their counts.
