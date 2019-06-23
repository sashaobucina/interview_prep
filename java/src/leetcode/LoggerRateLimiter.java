package leetcode;

import java.util.HashMap;
import java.util.Map;

public class LoggerRateLimiter {

  private Map<String, Integer> messages;

  public LoggerRateLimiter() {
    this.messages = new HashMap<>();
  }

  public LoggerRateLimiter(Map<String, Integer> messages) {
    this.messages = messages;
  }

  public boolean shouldPrint(int timestamp, String message) {
    if (timestamp - 10 < this.messages.getOrDefault(message, -11)) {
      return false;
    }
    this.messages.put(message, timestamp);
    return true;
  }

  public static void main(String[] args) {
    Map<String, Integer> messages = new HashMap<>();
    messages.put("foo", 1);

    LoggerRateLimiter lrl = new LoggerRateLimiter(messages);
    System.out.print(lrl.shouldPrint(11, "foo"));
  }
}