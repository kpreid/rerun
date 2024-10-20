// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/store/re_types/definitions/rerun/blueprint/archetypes/dataframe_query.fbs".

#pragma once

#include "../../blueprint/components/apply_latest_at.hpp"
#include "../../blueprint/components/filter_by_range.hpp"
#include "../../blueprint/components/filter_is_not_null.hpp"
#include "../../blueprint/components/selected_columns.hpp"
#include "../../blueprint/components/timeline_name.hpp"
#include "../../collection.hpp"
#include "../../compiler_utils.hpp"
#include "../../component_batch.hpp"
#include "../../indicator_component.hpp"
#include "../../result.hpp"

#include <cstdint>
#include <optional>
#include <utility>
#include <vector>

namespace rerun::blueprint::archetypes {
    /// **Archetype**: The query for the dataframe view.
    struct DataframeQuery {
        /// The timeline for this query.
        ///
        /// If unset, the timeline currently active on the time panel is used.
        std::optional<rerun::blueprint::components::TimelineName> timeline;

        /// If provided, only rows whose timestamp is within this range will be shown.
        ///
        /// Note: will be unset as soon as `timeline` is changed.
        std::optional<rerun::blueprint::components::FilterByRange> filter_by_range;

        /// If provided, only show rows which contains a logged event for the specified component.
        std::optional<rerun::blueprint::components::FilterIsNotNull> filter_is_not_null;

        /// Should empty cells be filled with latest-at queries?
        std::optional<rerun::blueprint::components::ApplyLatestAt> apply_latest_at;

        /// Selected columns. If unset, all columns are selected.
        std::optional<rerun::blueprint::components::SelectedColumns> select;

      public:
        static constexpr const char IndicatorComponentName[] =
            "rerun.blueprint.components.DataframeQueryIndicator";

        /// Indicator component, used to identify the archetype when converting to a list of components.
        using IndicatorComponent = rerun::components::IndicatorComponent<IndicatorComponentName>;

      public:
        DataframeQuery() = default;
        DataframeQuery(DataframeQuery&& other) = default;

        /// The timeline for this query.
        ///
        /// If unset, the timeline currently active on the time panel is used.
        DataframeQuery with_timeline(rerun::blueprint::components::TimelineName _timeline) && {
            timeline = std::move(_timeline);
            // See: https://github.com/rerun-io/rerun/issues/4027
            RR_WITH_MAYBE_UNINITIALIZED_DISABLED(return std::move(*this);)
        }

        /// If provided, only rows whose timestamp is within this range will be shown.
        ///
        /// Note: will be unset as soon as `timeline` is changed.
        DataframeQuery with_filter_by_range(
            rerun::blueprint::components::FilterByRange _filter_by_range
        ) && {
            filter_by_range = std::move(_filter_by_range);
            // See: https://github.com/rerun-io/rerun/issues/4027
            RR_WITH_MAYBE_UNINITIALIZED_DISABLED(return std::move(*this);)
        }

        /// If provided, only show rows which contains a logged event for the specified component.
        DataframeQuery with_filter_is_not_null(
            rerun::blueprint::components::FilterIsNotNull _filter_is_not_null
        ) && {
            filter_is_not_null = std::move(_filter_is_not_null);
            // See: https://github.com/rerun-io/rerun/issues/4027
            RR_WITH_MAYBE_UNINITIALIZED_DISABLED(return std::move(*this);)
        }

        /// Should empty cells be filled with latest-at queries?
        DataframeQuery with_apply_latest_at(
            rerun::blueprint::components::ApplyLatestAt _apply_latest_at
        ) && {
            apply_latest_at = std::move(_apply_latest_at);
            // See: https://github.com/rerun-io/rerun/issues/4027
            RR_WITH_MAYBE_UNINITIALIZED_DISABLED(return std::move(*this);)
        }

        /// Selected columns. If unset, all columns are selected.
        DataframeQuery with_select(rerun::blueprint::components::SelectedColumns _select) && {
            select = std::move(_select);
            // See: https://github.com/rerun-io/rerun/issues/4027
            RR_WITH_MAYBE_UNINITIALIZED_DISABLED(return std::move(*this);)
        }
    };

} // namespace rerun::blueprint::archetypes

namespace rerun {
    /// \private
    template <typename T>
    struct AsComponents;

    /// \private
    template <>
    struct AsComponents<blueprint::archetypes::DataframeQuery> {
        /// Serialize all set component batches.
        static Result<std::vector<ComponentBatch>> serialize(
            const blueprint::archetypes::DataframeQuery& archetype
        );
    };
} // namespace rerun
