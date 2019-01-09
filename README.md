

# Python-Backrub

PageRank works by counting the number and quality of links to a page to determine a rough estimate of how important the website is. The underlying assumption is that more important websites are likely to receive more links from other websites. Currently, PageRank is not the only algorithm used by Google to order search results, but it is the first algorithm that was used by the company, and it is the best known.

Quoting from the original Google paper, PageRank is defined like this:

> We assume page A has pages T1...Tn which point to it (i.e., are citations). The parameter d is a damping factor which can be set between 0 and 1. We usually set d to 0.85. There are more details about d in the next section. Also C(A) is defined as the number of links going out of page A. The PageRank of a page A is given as follows:
>  **PR(A) = (1-d) + d (PR(T1)/C(T1) + ... + PR(Tn)/C(Tn))**
>  Note that the PageRanks form a probability distribution over web pages, so the sum of all web pages' PageRanks will be one.
>  PageRank or PR(A) can be calculated using a simple iterative algorithm, and corresponds to the principal eigenvector of the normalized link matrix of the web.




More about PageRank : [Google PageRank](http://infolab.stanford.edu/~backrub/google.html)

# About the Project
The project implements the basic PageRank algorithm presented in the paper by Page and Brin.
 
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
Clone the repo using 
```
git clone https://github.com/rj1997/Python-Backrub.git
```

### Prerequisites

Python3 will do.

## Running the tests

To run each simulation use the following command from terminal:

```
python3 pagerank.py
```

## Contributing

The work is still in progress, I will add more functionalities to this algorithm in some time.
But you are free to make pull requests and start commiting.


## Authors

* **Rishabh Jain** - *LinkedIn* - [rj1997](https://www.linkedin.com/in/rj1997/)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* A wonderful page that get me started [PageRank with examples](https://www.cs.princeton.edu/~chazelle/courses/BIB/pagerank.htm)
* etc

