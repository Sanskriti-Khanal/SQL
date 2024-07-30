package controller;

import view.RegisterPage;
import view.LoginView;
import dao.UserDao;
import model.User;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class RegisterController {
    private RegisterPage view;
    private UserDao userDao;

    public RegisterController(RegisterPage view, UserDao userDao) {
        this.view = view;
        this.userDao = userDao;
        this.view.getRegisterButton().addActionListener(new RegisterButtonListener());
    }

    class RegisterButtonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            String email = view.getEmail();
            String password = view.getPassword();
            String confirmPassword = view.getConfirmPassword();
            String role = view.getRole();

            if (!password.equals(confirmPassword)) {
                JOptionPane.showMessageDialog(view, "Passwords do not match.");
                return;
            }

            User user = new User();
            user.setEmail(email);
            user.setPassword(password);
            user.setRole(role);

            boolean success = userDao.addUser(user);
            if (success) {
                JOptionPane.showMessageDialog(view, "Registration successful! Redirecting to login page.");
                new LoginController(new LoginView(), userDao);
                view.dispose();
            } else {
                JOptionPane.showMessageDialog(view, "Registration failed. Please try again.");
            }
        }
    }
}
