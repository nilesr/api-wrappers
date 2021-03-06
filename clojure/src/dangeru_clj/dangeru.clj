(ns dangeru-clj.dangeru
  (:require [clj-http.client :as client]
            [cheshire.core :as json]))

;; Replace newlines with spaces and remove carriage returns entirely
(defn purge-newlines [string]
  (clojure.string/replace (clojure.string/replace string #"\n" " ") #"\r" ""))

;; Get a (JSON) string of the last [limit] threads in [board]
(defn fetch-index [board limit]
  (:body (client/get "https://boards.dangeru.us/api.php?" 
                     {:query-params {:type "index" :board board :ln limit}
                      :insecure? true
                      :as :string})))

;; Ask for the last [limit] threads in [board], eliminate newlines, convert the resulting string
;;  to a clojure map
(defn index [board limit]
  (json/parse-string (purge-newlines (fetch-index board limit)) true))

;; Get a (JSON) string of the first [limit] posts in thread [id] from board [board]
(defn fetch-thread [board limit id]
  (:body (client/get "https://boards.dangeru.us/api.php?"
                     {:query-params {:type "thread" :board board :ln limit :thread id}
                      :insecure? true
                      :as :string})))

;; Ask for the first [limit] posts in thread [id] from board [board], eliminate newlines, convert
;;  the resulting string to a clojure map
(defn thread [board limit id]
  (json/parse-string (purge-newlines (fetch-thread board limit id)) true))
