package smart_clinc;

import view.LoginView;
import controller.LoginController;
import dao.UserDao;

public class Main {
    public static void main(String[] args) {
        LoginView view = new LoginView();
        UserDao userDao = new UserDao();
        new LoginController(view, userDao);
        view.setVisible(true);
    }
}
