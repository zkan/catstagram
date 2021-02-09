package team.odds.catstagram

import org.assertj.core.api.Assertions.assertThat
import org.junit.jupiter.api.Test
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.context.SpringBootTest
import org.springframework.boot.test.web.client.TestRestTemplate
import org.springframework.boot.test.web.client.getForEntity
import org.springframework.http.HttpStatus

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class CatListControllerTest(@Autowired val restTemplate: TestRestTemplate) {

    @Test
    fun `Assert status code and content`() {
        val entity = restTemplate.getForEntity<String>("/cats")
        assertThat(entity.statusCode).isEqualTo(HttpStatus.OK)
        assertThat(entity.body).contains("Salee")
    }

}