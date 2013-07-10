class Location < ActiveRecord::Base
  attr_accessible :aliases, :feature_class, :latitude, :longitude, :preferred_names

  has_and_belongs_to_many :children,
    class_name: 'LocationRelationship',
    join_table: 'location_relationships',
    foreign_key: 'parent_location_id',
    association_foreign_key: 'child_location_id'

  has_and_belongs_to_many :parents,
    class_name: 'LocationRelationship',
    join_table: 'location_relationships',
    foreign_key: 'child_location_id',
    association_foreign_key: 'parent_location_id'

  searchable do
    text(:preferred_names)
    text(:aliases)
    string(:feature_class)
    latlon(:location) { Sunspot::Util::Coordinates.new(latitude, longitude) }
  end
end
