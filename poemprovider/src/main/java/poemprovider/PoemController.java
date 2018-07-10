package poemprovider;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import poemprovider.dto.PoemDTO;

@RestController
public class PoemController {

	@GetMapping("/poem")
	public PoemDTO poem() {
		PoemDTO poemDTO = new PoemDTO();
		return poemDTO;
	}
}
