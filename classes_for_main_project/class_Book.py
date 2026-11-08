class Book():
    total_books = 0
    

    def __init__(self,name,author,copies):
        self.name = name
        self.author = author
        if copies < 1:
            raise ValueError("copies must be at least 1")
        self.copies = copies
        self.available = copies
        Book.total_books += 1
        # self.available.append({"name":name,"author":author,"available_copies":copies})
        

    def borrow(self):
        if self.available <= 0:
            raise ValueError("no copies available")
        self.available -= 1

    def return_book(self):
        if self.available == self.copies:
            raise ValueError("all copies are already in")
        self.available += 1

    def is_available(self):
        if self.available >= 1:
            return True
        else:
            return False
    def __str__(self):
        return f"{self.name} by {self.author} ({self.available}/{self.copies} available)"

    
