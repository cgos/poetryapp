package poemspringgateway.gateway;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.gateway.route.RouteLocator;
import org.springframework.cloud.gateway.route.builder.RouteLocatorBuilder;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class GatewayApplication {

	@Bean
	public RouteLocator customRouteLocator(RouteLocatorBuilder builder) {
		// @formatter:off
		return builder.routes()
				.route("poem", r -> r.path("/poem").uri("http://localhost:8181"))
				.route("bio", r -> r.path("/poetbio").uri("http://localhost:8888"))
				.route("poetry", r -> r.path("/poetry").uri("http://localhost:8080"))
				.build();
		// @formatter:on
	}

	public static void main(String[] args) {
		SpringApplication.run(GatewayApplication.class, args);
	}
}
