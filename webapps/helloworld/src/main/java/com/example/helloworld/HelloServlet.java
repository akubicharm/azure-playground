package com.example.helloworld;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class HelloServlet extends HttpServlet {

  private static final Logger logger = LogManager.getLogger(HelloServlet.class);

  public void doGet (HttpServletRequest req, HttpServletResponse res)
    throws ServletException, IOException {

    logger.info("doGet");
    logger.error("ERROR DOGET");
    PrintWriter out;

    res.setContentType("text/html; charset=Shift_JIS");
    out = res.getWriter();

    out.println("<html><body>");
    out.println("<h1>Hello World!</h1>");
    out.println("<p>Servletのサンプル（HelloServlet.java）</p>");
    out.println("</body></html>");
  }
}
