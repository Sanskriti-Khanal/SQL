package controller;

import view.LoginView;
import dao.UserDao;
import model.User;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class LoginController {
    private LoginView view;
    private UserDao userDao;

    public LoginController(LoginView view, UserDao userDao) {
        this.view = view;
        this.userDao = userDao;
        this.view.getLoginButton().addActionListener(new LoginButtonListener());
        this.view.getRegisterButton().addActionListener(new RegisterButtonListener());
        this.view.getForgotButton().addActionListener(new ForgotButtonListener());
    }

    class LoginButtonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            String email = view.getEmail();
            String password = view.getPassword();
            String role = view.getRole();
            User user = userDao.getUser(email, password, role);
            if (user != null) {
                JOptionPane.showMessageDialog(view, "Login Successful!");
                // Proceed to the next screen based on role
            } else {
                JOptionPane.showMessageDialog(view, "Invalid email/password/role");
            }
        }
    }

    class RegisterButtonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            // Navigate to Register screen
            JOptionPane.showMessageDialog(view, "Navigate to Register screen");
        }
    }

    class ForgotButtonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            // Navigate to Forgot Password screen
            JOptionPane.showMessageDialog(view, "Navigate to Forgot Password screen");
        }
    }
}
