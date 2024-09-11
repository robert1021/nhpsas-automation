from menu import Menu
from menu_bar import MenuBar
from submission_module import SubmissionModule
from tracking_module import TrackingModule
from utilities import load_column_from_excel


def enter_nhpsas_discontinuation(submission_id, user_id, discontinuation_date, is_gowling):
    nhpsas_menu = Menu()
    nhpsas_menubar = MenuBar()

    # ----- Open Submission Module -----
    nhpsas_menu.open_submission_module()
    nhpsas_submission_module = SubmissionModule()
    nhpsas_submission_module.ignore_errors()
    nhpsas_submission_module.enter_submission_id(submission_id)
    nhpsas_submission_module.ignore_errors()
    nhpsas_submission_module.click_attributes_tab()
    nhpsas_submission_module.add_attribute_type_cancelled_by_licensee(discontinuation_date, is_gowling)
    nhpsas_submission_module.add_attribute_type_cancellation_notice(discontinuation_date, is_gowling)
    nhpsas_menubar.exit()

    # ----- Open Tracking Module -----
    nhpsas_menu.open_tracking_module()
    nhpsas_tracking_module = TrackingModule()
    nhpsas_tracking_module.enter_submission_id(submission_id)
    nhpsas_tracking_module.add_role_type_decision(user_id)
    nhpsas_tracking_module.click_tracking_tab()
    nhpsas_tracking_module.add_status_type_cancellation_of_licence(discontinuation_date, is_gowling)
    nhpsas_menubar.exit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    submissions_path = input("Enter Path Containing Submissions: ")
    nhpsas_user_id = input("Enter the NHPSAS User ID: ")
    date = input("Enter the Discontinuation Date: ")
    is_applicant_gowling = input("Is Applicant Contact Gowling? (y/n): ")

    is_applicant_gowling = True if is_applicant_gowling.lower() == "y" else False

    submissions = load_column_from_excel(submissions_path, "SUBMISSION")
    print(submissions)
    #
    # # TODO: Need to add logic into code to check if there is enough fields
    # # If there isnt click one of the fields and click the "Insert Record" button in menubar
    #
    for sub in submissions:
        print(f"Working on {sub}")
        enter_nhpsas_discontinuation(str(sub), nhpsas_user_id, date, is_applicant_gowling)
        print("-" * 50)
