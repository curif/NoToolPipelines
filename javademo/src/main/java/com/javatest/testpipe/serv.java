package com.javatest.testpipe;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

@RestController
public class serv {

	@RequestMapping("/")
	public String index() {
		return "Greetings from Spring Boot!";
    }
    
    @RequestMapping("/sum")
	public int sum(int a, int b) {
		return a+b;
	}

}