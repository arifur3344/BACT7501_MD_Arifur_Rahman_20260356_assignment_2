# purchase requisition system


# counter to give each requisition a different id (kept outside the class)
requisition_counter = 0

# all the requisitions get saved here so we can print them later
all_requisitions = []


class Requisition:

    # numbers for the statistics
    total_submitted = 0
    total_approved = 0
    total_pending = 0
    total_not_approved = 0

    def __init__(self):
        global requisition_counter

        # make the id
        requisition_counter = requisition_counter + 1
        self.requisition_id = requisition_counter + 10000

        # the shared data starts empty
        self.date = ""
        self.staff_id = ""
        self.staff_name = ""
        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"

    # ask the staff for their details and the items
    def add_requisition(self):
        print("Enter your information:")
        self.date = input("Date (DD/MM/YYYY): ")
        self.staff_id = input("Staff ID: ")
        self.staff_name = input("Staff Name: ")

        print("Requisition ID:", self.requisition_id)

        # ask for the items one by one
        print("Add items")
        self.total = 0
        while True:
            item_name = input("Item Name: ")
            item_price = float(input("Item Price ($): "))

            self.items.append({"name": item_name, "price": item_price})
            self.total = self.total + item_price

            add_more = input("Add another item (yes/no): ")
            if add_more == "no":
                break

        # save it and count it
        all_requisitions.append(self)
        Requisition.total_submitted = Requisition.total_submitted + 1
        Requisition.total_pending = Requisition.total_pending + 1

        print("Total: $" + format(self.total, ".2f"))
        return self.total

    # approve it if the total is under 500
    def approve_requisition(self):
        if self.total < 500:
            self.status = "Approved"

            # reference = staff id + last 3 digits of the requisition id
            last_three = str(self.requisition_id)[-3:]
            self.approval_reference = self.staff_id + last_three

            Requisition.total_pending = Requisition.total_pending - 1
            Requisition.total_approved = Requisition.total_approved + 1

        return self.status

    # manager answers a pending one
    def respond_to_requisition(self):
        # only answer if it is still pending
        if self.status != "Pending":
            return self.status

        print("Requisition", self.requisition_id, "total is $" + format(self.total, ".2f"))
        decision = input("Manager decision (approved/not approved/pending): ")
        decision = decision.lower()

        if decision == "approved":
            self.status = "Approved"

            last_three = str(self.requisition_id)[-3:]
            self.approval_reference = self.staff_id + last_three

            Requisition.total_pending = Requisition.total_pending - 1
            Requisition.total_approved = Requisition.total_approved + 1

        elif decision == "not approved":
            self.status = "Not approved"
            self.approval_reference = "Not available"

            Requisition.total_pending = Requisition.total_pending - 1
            Requisition.total_not_approved = Requisition.total_not_approved + 1

        else:
            # anything else means leave it as pending
            print("Requisition", self.requisition_id, "is left as pending.")

        return self.status

    # print one requisition
    def display_requisition(self):
        print("Date:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Total: $" + format(self.total, ".2f"))
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_reference)
        print()

    # print all the requisitions
    def display_all_requisitions(self):
        print("Displaying all requisitions")
        print("---------------------------")
        for req in all_requisitions:
            req.display_requisition()

    # show the statistics
    def requisition_statistics(self):
        print("Displaying the Requisition Statistics")
        print("The total number of requisitions submitted:", Requisition.total_submitted)
        print("The total number of approved requisitions:", Requisition.total_approved)
        print("The total number of pending requisitions:", Requisition.total_pending)
        print("The total number of not approved requisitions:", Requisition.total_not_approved)
        print()

