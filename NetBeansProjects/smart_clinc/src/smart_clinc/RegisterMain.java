package smart_clinc;

import view.RegisterPage;
import controller.RegisterController;
import dao.UserDao;

public class RegisterMain {
    public static void main(String[] args) {
        // Create the view
        RegisterPage view = new RegisterPage();

        // Create the DAO
        UserDao userDao = new UserDao();

        // Create the controller
        RegisterController controller = new RegisterController(view, userDao);

        // Set the view visible
        view.setVisible(true);
    }
}
