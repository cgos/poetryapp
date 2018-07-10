package poemprovider;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import poemprovider.dto.PoemDTO;

@RestController
public class PoemController {
	private org.slf4j.Logger logger = org.slf4j.LoggerFactory.getLogger(PoemController.class);;
	

	@GetMapping("/poem")
	@ResponseBody
	public PoemDTO poem() {
		PoemDTO poemDTO = new PoemDTO();
		logger.debug("/poem: " + poemDTO.toString());
		return poemDTO;
	}
}
